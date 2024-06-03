begin;
    create table newsletters(
        id uuid primary key,
        name text not null
    );

    create table subscriptions(
        id uuid primary key,
        newsletter_id uuid references newsletters,
        recipients text not null
    );
commit ;