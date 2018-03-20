# pydbmate
> Another Python migration tool

[![Build Status](https://travis-ci.org/hmleal/pydbmate.svg?branch=master)](https://travis-ci.org/hmleal/pydbmate)

This project is inspired by ```dbmate```

### Features

* Supports MySQL, PostgreSQL and SQLite

### Instalation

```sh
pip install pydbmate
```

### Commands

```sh
pydbmate            # print help
pydbmate new        # generate a new migration file
pydbmate migrate    # run any pending migrations
pydbmate roolback   # roll back the most recent migration
```

### TODO

- [ ] Create the project structure
- [ ] Set up Travis CI
- [ ] Generate a function to create new migration files
- [ ] Generate a function to parser migration file
