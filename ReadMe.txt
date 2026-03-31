Structure de base de données que je propose

1. Utilisateurs (Users)

Champ           Type            Description
id              INT             Identifiant unique
email           VARCHAR         Utilisé pour la connexion
password_hash   VARCHAR         Mot de passe sécurisé
role            ENUM            recruiter ou candidate
first_name      VARCHAR         Prénom
last_name       VARCHAR         Nom
phone           VARCHAR         Téléphone(optionnel au cas ou l'utilisateur ne veut donner que l'email)
avatar_url      TEXT            Photo de profil
created_at      DATETIME        Date d’inscription
is_active       BOOLEAN         Compte actif / désactivé

---

2. Profils recruteurs (RecruiterProfiles)
// FK signifie foreign key pour cle etrangere
Champ                   Type        Description
user_id                 INT (FK)    Lien vers users.id
company_name            VARCHAR     Nom de l’entreprise
company_website         VARCHAR     Site web
company_description     TEXT        Présentation de l’entreprise
position                VARCHAR     Poste du recruteur (ex: RH dans la majorite des entreprises)

---

3. Profils candidats (CandidateProfiles)

Champ                   Type        Description
user_id                 INT (FK)    Lien vers users.id
headline                VARCHAR     Titre professionnel (ex: Développeur Java)
bio TEXT                Courte      présentation
resume_url              TEXT        Lien vers le CV (PDF)
location                VARCHAR     Localisation
years_experience        INT         nobre Années d’expérience
skills                  TEXT        Liste de compétences
desired_job_types       TEXT        Types de postes recherchés 

---

4. Offres d’emploi (JobOffers)

Champ                   Type        Description
id                      internes    Identifiant unique
recruiter_id            INT (FK)    Lien vers users.id (ou recruiter_profiles.user_id)
title                   VARCHAR     Titre du poste
description             TEXT        Description détaillée
requirements            TEXT        Prérequis (compétences, diplômes, etc.)
location                VARCHAR     Lieu de travail (ou remote)
employment_type         ENUM        CDI, CDD, stage, freelance…
salary_min              DECIMAL     Fourchette basse
salary_max              DECIMAL     Fourchette haute
currency                VARCHAR     Devise (EUR, USD…)
experience_level        ENUM        Junior, Confirmé, Senior…
skills_required         JSON        Liste des compétences nécessaires
status                  ENUM        open, closed, draft
posted_at               DATETIME    Date de publication
expires_at              DATETIME    Date de fin de validité
views_count             INT         Nombre de vues (optionnel)

---

5. Candidatures (Applications)

Champ                   Type        Description
id                      INT         Identifiant unique
job_offer_id            INT (FK)    Lien vers job_offers.id
candidate_id            INT (FK)    Lien vers users.id
applied_at              DATETIME    Date de candidature
status                  ENUM        pending, reviewed, interview, rejected, hired
cover_letter            TEXT        Lettre de motivation
resume_version          TEXT        Lien vers le CV utilisé (si différent du profil)
recruiter_notes         TEXT        Notes internes du recruteur

---
!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// j'ai pas eu d'idee sur comment la mise en lien d'un recruteur et d'un candidat devrait se faire
// par exemple le candidat postule et puis en fonction des skills et caracteristiques le recruteur accepte
// en donnant l'opportunite d'un entretien , soit il rejete direct la demande
// ici on devrait gerer ca un peu comme la mise en lien grace a l'app 
// apres on pourra penser a developper un espace de chat
// si t'as une idee tu proposes


---

7. Sauvegardes / Favoris (SavedJobs)

Champ           Type        Description
candidate_id    INT (FK)    users.id
job_offer_id    INT (FK)    job_offers.id
saved_at        DATETIME    Date d’ajout

---
// ici il s'agit des notifs en cas d'une offre /chez le candidat
// et en cas de l'application d'un potentiel candidat / cote recruteur
// ainsi de suite
8. Notifications (Notifications)

Champ           Type        Description
id              INT         Identifiant unique
user_id         INT (FK)    users.id
type            VARCHAR     new_application, status_update, new_message…
content         TEXT        Message de la notification
is_read         BOOLEAN     Lecture
created_at      DATETIME    Date de création

---
// ici c'est le conseil que chatGpt m'a donné
9. Tables de référence (Tags / Catégories)

Secteurs (Industries)

· id (INT)
· name (VARCHAR)

Compétences (Skills)

· id (INT)
· name (VARCHAR)

Types de contrat (ContractTypes)

· id (INT)
· name (VARCHAR)

---

Relations principales (schéma simplifié)

```
Users
  ├─ RecruiterProfile (1-1)
  ├─ CandidateProfile (1-1)
  └─ JobOffers (1-n) — par le recruteur

JobOffers
  ├─ Applications (1-n) — avec Candidate
  └─ SavedJobs (1-n) — avec Candidate