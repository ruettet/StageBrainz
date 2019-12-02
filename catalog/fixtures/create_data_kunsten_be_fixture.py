from configparser import ConfigParser
import psycopg2
from json import dump
from codecs import open
from datetime import datetime


fixture = []

cfg = ConfigParser()
cfg.read("catalog/fixtures/db.cfg")
knst = psycopg2.connect(host=cfg['db']['host'], port=cfg['db']['port'],
                        database=cfg['db']['db'], user=cfg['db']['user'],
                        password=cfg['db']['pwd'])
knst.set_client_encoding('UTF-8')

# Seasons
sql = """
SELECT DISTINCT id, name, start_year, end_year
FROM production.seasons

"""

cur = knst.cursor()
cur.execute(sql)

seasons_id_pk = {}
i = 1
for row in cur.fetchall():
    id, name, start_year, end_year = row
    data = {
        "pk": i,
        "model": "catalog.Season",
        "fields": {
            "name": name,
            "start_date": str(start_year),
            "end_date": str(end_year)
        }
    }
    fixture.append(data)
    seasons_id_pk[id] = i
    i += 1

# Productions
sql = """
SELECT DISTINCT p.id, p.title, p.season_id
FROM production.productions p
JOIN production.production_types_productions ptp ON ptp.production_id = p.id
WHERE ptp.production_type_id = 31 
"""

cur = knst.cursor()
cur.execute(sql)

productions_id_pk = {}
i = 1
for row in cur.fetchall():
    id, title, season_id = row
    data = {
        "pk": i,
        "model": "catalog.EntityProduction",
        "fields": {
            "name": title if title else "Not set",
            "sort_name": title if title else "Not set",
            "disambiguation": title if title else "Not set",
            "season": seasons_id_pk[season_id] if season_id else None
        }
    }
    fixture.append(data)
    productions_id_pk[id] = i
    i += 1

# Genres
sql = """
SELECT DISTINCT g.id, g.name_nl
FROM production.genres g
"""

cur = knst.cursor()
cur.execute(sql)

genres_id_pk = {}
i = 1
for row in cur.fetchall():
    id, name = row
    data = {
        "pk": i,
        "model": "catalog.EntityGenre",
        "fields": {
            "name": name if name else "Not set",
            "sort_name": name if name else "Not set",
            "disambiguation": name if name else "Not set"
        }
    }
    fixture.append(data)
    genres_id_pk[id] = i
    i += 1

# Shows
sql = """
SELECT DISTINCT s.id, d.year, d.month, d.day, time, p.title, v.name
FROM production.shows s
JOIN production.date_isaars d ON d.id = s.date_id 
JOIN production.productions p ON s.production_id = p.id
JOIN production.venues v ON s.venue_id = v.id

"""

cur = knst.cursor()
cur.execute(sql)

shows_id_pk = {}
i = 1
for row in cur.fetchall():
    id, year, month, day, time, title, venue = row
    day = day if day else 1
    month = month if month and month > 0 else 1
    if title and venue:
        name = title + " in " + venue
    elif title is None and venue:
        name = "No production, but in " + venue
    elif venue is None and title:
        name = title + "in unknown venue"
    else:
        name = "No production or venue information"

    if year is None or year < 1:
        when_date = None
    elif month is None or month < 1:
        when_date = str(year)
    elif day is None or day < 1:
        when_date = str(year) + "-" + str(month)
    else:
        when_date = str(year) + "-" + str(month) + "-" + str(day)

    if time and ":" in time and len(time) == 5:
        try:
            when_time = datetime(1970, 1, 1, int(time[0:2]), int(time[3:])).time().isoformat()
        except Exception as e:
            when_time = None

    data = {
        "pk": i,
        "model": "catalog.EntityShow",
        "fields": {
            "name": name if name else "Not set",
            "sort_name": name if name else "Not set",
            "disambiguation": name + " - " + when_date if when_date else name,
            "when_date": when_date,
            "when_time": when_time
        }
    }
    fixture.append(data)
    shows_id_pk[id] = i
    i += 1

# shows to productions
sql = """
SELECT DISTINCT s.id, s.production_id
FROM production.shows s

"""

cur = knst.cursor()
cur.execute(sql)

i = 1
for row in cur.fetchall():
    show_id, prod_id = row
    if prod_id and prod_id in productions_id_pk and show_id and show_id in shows_id_pk:
        data = {
            "pk": i,
            "model": "catalog.RelationShowProduction",
            "fields": {
                "entity_a": shows_id_pk[show_id],
                "entity_b": productions_id_pk[prod_id],
                "relation_type": [1]
            }
        }
        fixture.append(data)
        i += 1

# people
sql = """
SELECT DISTINCT p.id, p.full_name, p.first_name, p.name, birthd.year, birthd.month, birthd.day, deathd.year, deathd.month, deathd.day
FROM production.people p
LEFT JOIN production.date_isaars birthd ON birthd.id = p.birthdate_id
LEFT JOIN production.date_isaars deathd ON deathd.id = p.death_date_id
JOIN production.relationships r ON r.person_id = p.id
WHERE r.production_id IS NOT NULL OR r.book_title_id IS NOT NULL 

"""

cur = knst.cursor()
cur.execute(sql)

organity = 1
people_id_pk = {}
for row in cur.fetchall():
    id, name, first_name, last_name, birthy, birthm, birthd, deathy, deathm, deathd = row
    try:
        start = datetime(birthy, birthm, birthd).date().isoformat()
    except (TypeError, ValueError):
        start = None

    try:
        end = datetime(deathy, deathm, deathd).date().isoformat()
    except (TypeError, ValueError):
        end = None

    if last_name and first_name:
        sort_name = last_name + ", " + first_name
    else:
        sort_name = name

    data = {
        "pk": organity,
        "model": "catalog.EntityOrganity",
        "fields": {
            "name": name if name else "Not set",
            "sort_name": sort_name if sort_name else "Not set",
            "start_date": start,
            "end_date": end,
            "entity_type": [1]
        }
    }
    fixture.append(data)
    people_id_pk[id] = organity
    organity += 1


# people to productions
sql = """
SELECT DISTINCT r.person_id, r.production_id, f.name_nl, r.vip
FROM production.relationships r
LEFT JOIN production.functions f ON r.function_id = f.id
WHERE r.person_id IS NOT NULL AND r.production_id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

relation_production_organity = 1
for row in cur.fetchall():
    person_id, prod_id, func, vip = row
    if prod_id and prod_id in productions_id_pk:
        data = {
            "pk": relation_production_organity,
            "model": "catalog.RelationProductionOrganity",
            "fields": {
                "entity_a": productions_id_pk[prod_id],
                "entity_b": people_id_pk[person_id],
                "relation_name": func,
                "highlighted_relation": vip
            }
        }
        fixture.append(data)
        relation_production_organity += 1

# genres to productions
sql = """
SELECT DISTINCT r.genre_id, r.production_id
FROM production.relationships r
WHERE r.genre_id IS NOT NULL AND r.production_id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

relation_production_genre = 1
for row in cur.fetchall():
    genre_id, prod_id = row
    if prod_id and prod_id in productions_id_pk:
        data = {
            "pk": relation_production_genre,
            "model": "catalog.RelationProductionGenre",
            "fields": {
                "entity_a": productions_id_pk[prod_id],
                "entity_b": genres_id_pk[genre_id],
                "relation_type": [1]
            }
        }
        fixture.append(data)
        relation_production_genre += 1

# organisations
sql = """
SELECT DISTINCT p.id, p.name, birthd.year, birthd.month, birthd.day, deathd.year, deathd.month, deathd.day
FROM production.organisations p
LEFT JOIN production.date_isaars birthd ON birthd.id = p.start_activities_date_id
LEFT JOIN production.date_isaars deathd ON deathd.id = p.end_activities_date_id
JOIN production.relationships r ON r.organisation_id = p.id
JOIN production.productions prod ON r.production_id = prod.id
JOIN production.production_types_productions ptp ON ptp.production_id = prod.id
WHERE ptp.production_type_id = 31

"""

cur = knst.cursor()
cur.execute(sql)

organisations_id_pk = {}
for row in cur.fetchall():
    id, name, birthy, birthm, birthd, deathy, deathm, deathd = row
    try:
        start = datetime(birthy, birthm, birthd).date().isoformat()
    except (TypeError, ValueError):
        start = None

    try:
        end = datetime(deathy, deathm, deathd).date().isoformat()
    except (TypeError, ValueError):
        end = None

    data = {
        "pk": organity,
        "model": "catalog.EntityOrganity",
        "fields": {
            "name": name if name else "Not set",
            "sort_name": name if sort_name else "Not set",
            "start_date": start,
            "end_date": end,
            "entity_type": [4]
        }
    }
    fixture.append(data)
    organisations_id_pk[id] = organity
    organity += 1


# works
sql = """
SELECT DISTINCT w.id, w.title_nl, w.publication_year
FROM production.book_titles w
WHERE w.class_name = 'TheaterText'
"""

cur = knst.cursor()
cur.execute(sql)

works_id_pk = {}
i = 1
for row in cur.fetchall():
    id, title, pubyear = row
    data = {
        "pk": i,
        "model": "catalog.EntityWork",
        "fields": {
            "name": title if name else "Not set",
            "sort_name": title if sort_name else "Not set",
            "disambiguation": title if sort_name else "Not set",
            "start_date": pubyear if pubyear else "Not set",
            "entity_type": [1]
        }
    }
    fixture.append(data)
    works_id_pk[id] = i
    i += 1


# organisations to productions
sql = """
SELECT DISTINCT r.organisation_id, r.production_id, f.name_nl
FROM production.relationships r
LEFT JOIN production.functions f ON r.function_id = f.id
WHERE r.organisation_id IS NOT NULL AND r.production_id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

for row in cur.fetchall():
    organisation_id, prod_id, func = row
    if prod_id and prod_id in productions_id_pk and organisation_id and organisation_id in organisations_id_pk:
        data = {
            "pk": relation_production_organity,
            "model": "catalog.RelationProductionOrganity",
            "fields": {
                "entity_a": productions_id_pk[prod_id],
                "entity_b": organisations_id_pk[organisation_id],
                "relation_name": func,
                "highlighted_relation": func == "gezelschap"
            }
        }
        fixture.append(data)
        relation_production_organity += 1

# productions to works
sql = """
SELECT DISTINCT r.book_title_id, r.production_id
FROM production.relationships r
WHERE r.book_title_id IS NOT NULL AND r.production_id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

relation_production_work = 1
for row in cur.fetchall():
    work_id, prod_id = row
    if prod_id and prod_id in productions_id_pk and work_id and work_id in works_id_pk:
        data = {
            "pk": relation_production_work,
            "model": "catalog.RelationProductionWork",
            "fields": {
                "entity_a": productions_id_pk[prod_id],
                "entity_b": works_id_pk[work_id],
                "relation_type": [1],
            }
        }
        fixture.append(data)
        relation_production_work += 1

# organities (people) to works
sql = """
SELECT DISTINCT r.book_title_id, r.person_id
FROM production.relationships r
WHERE r.book_title_id IS NOT NULL AND r.person_id IS NOT NULL AND r.type = 'BookTitleByPerson'

"""

cur = knst.cursor()
cur.execute(sql)

relation_organity_work = 1
for row in cur.fetchall():
    work_id, person_id = row
    if person_id and person_id in people_id_pk and work_id and work_id in works_id_pk:
        data = {
            "pk": relation_organity_work,
            "model": "catalog.RelationOrganityWork",
            "fields": {
                "entity_a": people_id_pk[person_id],
                "entity_b": works_id_pk[work_id],
                "relation_type": [1],
                "highlighted_relation": True
            }
        }
        fixture.append(data)
        relation_organity_work += 1

# venues
sql = """
SELECT DISTINCT p.id, p.name
FROM production.venues p

"""

cur = knst.cursor()
cur.execute(sql)

venues_id_pk = {}
for row in cur.fetchall():
    id, name = row

    data = {
        "pk": organity,
        "model": "catalog.EntityOrganity",
        "fields": {
            "name": name if name else "Not set",
            "sort_name": name if name else "Not set",
            "entity_type": [2]
        }
    }
    fixture.append(data)
    venues_id_pk[id] = organity
    organity += 1


# show to venue
sql = """
SELECT DISTINCT r.venue_id, r.id
FROM production.shows r
WHERE r.venue_id IS NOT NULL AND r.id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

relation_show_organity = 1
for row in cur.fetchall():
    venue_id, show_id = row
    if show_id and show_id in shows_id_pk and venue_id and venue_id in venues_id_pk:
        data = {
            "pk": relation_show_organity,
            "model": "catalog.RelationShowOrganity",
            "fields": {
                "entity_a": shows_id_pk[show_id],
                "entity_b": venues_id_pk[venue_id],
                "relation_type": [1]
            }
        }
        fixture.append(data)
        relation_show_organity += 1

# show to festival
sql = """
SELECT DISTINCT r.organisation_id, r.id
FROM production.shows r
WHERE r.venue_id IS NOT NULL AND r.id IS NOT NULL

"""

cur = knst.cursor()
cur.execute(sql)

relation_show_organity = 1
for row in cur.fetchall():
    venue_id, show_id = row
    if show_id and show_id in shows_id_pk and venue_id and venue_id in venues_id_pk:
        data = {
            "pk": relation_show_organity,
            "model": "catalog.RelationShowOrganity",
            "fields": {
                "entity_a": shows_id_pk[show_id],
                "entity_b": venues_id_pk[venue_id],
                "relation_type": [1]
            }
        }
        fixture.append(data)
        relation_show_organity += 1

# organity to organity
sql = """
SELECT DISTINCT from_id, to_id, organisation_relation_type_id
FROM production.organisation_relations
"""

cur = knst.cursor()
cur.execute(sql)

relation_organity_organity_type = {
    124: 1,
    125: 2,
    127: 3,
    128: 4,
    129: 5,
    130: 4,
    126: 6
}

relation_organity_organity = 1
for row in cur.fetchall():
    from_id, to_id, reltype = row
    if from_id and from_id in organisations_id_pk and to_id and to_id in organisations_id_pk and reltype:
        data = {
            "pk": relation_organity_organity,
            "model": "catalog.RelationOrganityOrganity",
            "fields": {
                "entity_a": organisations_id_pk[to_id],
                "entity_b": organisations_id_pk[from_id],
                "relation_type": [relation_organity_organity_type[reltype]]
            }
        }
        fixture.append(data)
        relation_organity_organity += 1

with open("catalog/fixtures/data_kunsten_be.json", "w", "utf-8") as f:
    dump(fixture, f, indent=4)
