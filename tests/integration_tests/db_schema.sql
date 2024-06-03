begin;
    create table newsletters(
        id uuid primary key,
        name text not null,
        file_path text
    );

    create table subscriptions(
        id uuid primary key,
        newsletter_id uuid references newsletters not null ,
        recipient_id uuid references recipients not null
    );

    create table recipients(
       email text primary key
    );

commit ;