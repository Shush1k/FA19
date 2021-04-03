from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    ForeignKey,
    create_engine,
    Float,
    insert
)
from sqlalchemy.sql import select
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///Students.db')
metadata = MetaData()
connection = engine.connect()

student = Table('student', metadata, autoload=True, autoload_with=engine)
university = Table('university', metadata, autoload=True, autoload_with=engine)


# Вставка данных
ins_university = insert(university).values(
    univ_id=9,
    univ_name='FA',
    rating=330,
    city='Москва'
)

ins_student = insert(student).values(
    student_id=2,
    surname='Баранов',
    name='Александр',
    stipend=0,
    kurs=2,
    city='Москва',
    birthday=datetime(1980, 12, 1),
    univ_id=9
)

ins_next_student = insert(student).values(
    student_id=2,
    surname='Баранов',
    name='Андрей',
    stipend=0,
    kurs=2,
    city='Москва',
    birthday=datetime(1980, 12, 1),
    univ_id=22
)

# начинаем транзакцию БД
transaction = connection.begin()

# Добавление записей
connection.execute(ins_student)
connection.execute(ins_university)

try:
    connection.execute(ins_next_student)
except IntegrityError as e:
    # откат транзакции в начальное состояние в случае ошибки
    transaction.rollback()
    print("ОШИБКА добавления нового студента:\n", e)
