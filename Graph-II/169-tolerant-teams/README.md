## tolerant teams

Write a function, *tolerant_teams*, that takes in a list of rivalries as an argument. A rivalry is
a pair of people who should not be placed on the same team. The function should return a boolean
indicating whether or not it is possible to separate people into two teams, without rivals being on
the same team. The two teams formed do not have to be the same size.

#### test_00:

```python
tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
]) # -> True
```

#### test_01:

```python
tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader'),
  ('raj', 'philip'),
  ('seb', 'raj')
]) # -> False
```

#### test_02:

```python
tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) # -> True
```

#### test_03:

```python
tolerant_teams([
  ('alex', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) # -> False
```

#### test_04:

```python
tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> True
```

#### test_05:

```python
tolerant_teams([
  ('alan', 'jj'),
  ('jj', 'richard'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> True
```

#### test_06:

```python
tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('betty', 'christine'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) # -> False
```

#### test_07:

```python
tolerant_teams([
  ['ara', 'boyka'],
  ['dennis', 'clara'],
  ['boyka', 'clara']
]) # -> True
```
