DROP TABLE attendances;
DROP TABLE members;
DROP TABLE activities;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    instructor VARCHAR(255),
    time timestamp(0) without time zone,
    studio VARCHAR(255),
    level VARCHAR(255),
    capacity INT
);

CREATE TABLE attendances (
  id SERIAL PRIMARY KEY,
  member_id INT REFERENCES members(id) ON DELETE CASCADE,
  activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);