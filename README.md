# StageBrainz
A musicbrainz-inspired database for performing arts (theatre, dance, etc.)

# Mission
StageBrainz aims to be an open, free, online, crowdsourced overview of the performing arts.

# Data Model
As in Musicbrainz, StageBrainz has a limited number of core entities:
- Organities: persons, organisations, venues, etc. active in performing arts
- Productions: a stage production that will be performed repeatedly over the course of a season
- Shows: the actual performances of a stage production
- Works: conceptual creations, e.g. a theater text, from which stage productions can be derived
- Characters: fictional characters in works, e.g. Hamlet

And a number of auxiliary entities
- Genres: all sorts of genres for performing arts, e.g. dance, theater, theater for a young audience, ...
- Languages: ISO list of languages
- Locations: free street address text fields, with fixed city and country level
- Urls: links to online resources

Every core entity has a disambiguation line. Because of this, entities with duplicate names can have a disambiguation string in representation, e.g. 'Ancienne Belgique (Concert hall in Brussels)'.

Each entity, so both the core as well as the auxiliary entities, has a related X_type, e.g. a person (member of people) can be of type 'Actor' (a person_type).

INSERT UML TO SHOW TYPE RELATION

The core entities can also have an Alias of a certain AliasType. As an example, the Venue 'Ancienne Belgique' is 'abbreviated as' (i.e. the AliasType) 'AB'.
 
INSERT UML TO SHOW ALIAS + ALIASTYPE RELATION 

Furthermore, each entity can be related to all other entities, including itself. It is therefore possible to make every kind of relation:

|              | Organities   | Works        | Characters   | Poductions   | Shows        | Genres       | Languages    | Locations    | Urls |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ---- |
| Organities   | x            |              |              |              |              |              |              |              |      |
| Works        | x            | x            |              |              |              |              |              |              |      |
| Characters   | x            | x            | x            |              |              |              |              |              |      |
| Productions  | x            | x            | x            | x            |              |              |              |              |      |
| Shows        | x            | x            | x            | x            | x            |              |              |              |      |
| Genres       | x            | x            | x            | x            | x            | x            |              |              |      |
| Languages    | x            | x            | x            | x            | x            | x            | x            |              |      |
| Locations    | x            | x            | x            | x            | x            | x            | x            | x            |      |
| Urls         | x            | x            | x            | x            | x            | x            | x            | x            | x    |

Every relation in itself has a Type.

INSERT UML TO SHOW RELATION + RELATIONTYPE

Because of this, it is possible to distinguish between a (semantic) value of a relation, and the way in which the relation is presented. As an example, an Actor who performs a role in a stage production can be credited as 'with'; in this model, it is possible to represent the relation between the Actor and the Production with a RelationActorProduction of the Type 'Actor', while the Relation carries the name 'with'.
