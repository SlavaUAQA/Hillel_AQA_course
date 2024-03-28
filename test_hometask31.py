import pytest

def test_maxweight(fixture_sql):
    cursor = fixture_sql
    cursor.execute("SELECT * FROM boxers ORDER BY weight")
    result = cursor.fetchone()
    assert "Usyk Olexander" in result
