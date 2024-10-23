# Magnificent 7 API

This project provides an API to fetch the "Magnificent 7" team based on a player's combined goals and assists. The "Magnificent 7" team consists of:
- 1 goalkeeper
- 2 defenders
- 3 midfielders
- 1 forward

Players are selected based on their **magnificence** (the sum of goals scored and assists). The data is fetched from an external Fantasy Premier League API.

## API Endpoints

### 1. Get the Overall "Magnificent 7" Team

**Endpoint**: `/magnificent-7`

**Description**: `GET` Request that returns the 7-a-side team with the highest magnificence (combined goals and assists).

#### Example Response:

```json
{
  "goalkeeper": {
    "first_name": "John",
    "last_name": "Doe",
    "web_name": "J.Doe",
    "goals_scored": 0,
    "assists": 1
  },
  "defenders": [
    {
      "first_name": "Jane",
      "last_name": "Smith",
      "web_name": "J.Smith",
      "goals_scored": 2,
      "assists": 3
    },
    {
      "first_name": "Joe",
      "last_name": "Bloggs",
      "web_name": "J.Bloggs",
      "goals_scored": 1,
      "assists": 2
    }
  ],
  "midfielders": [
    {
      "first_name": "Alice",
      "last_name": "Jones",
      "web_name": "A.Jones",
      "goals_scored": 5,
      "assists": 4
    },
    {
      "first_name": "Bob",
      "last_name": "White",
      "web_name": "B.White",
      "goals_scored": 3,
      "assists": 6
    },
    {
      "first_name": "Charlie",
      "last_name": "Brown",
      "web_name": "C.Brown",
      "goals_scored": 4,
      "assists": 3
    }
  ],
  "forward": {
    "first_name": "Dave",
    "last_name": "Thomas",
    "web_name": "D.Thomas",
    "goals_scored": 10,
    "assists": 7
  }
}
```

### 2. Get the "Magnificent 7" for a Specific Team

**Endpoint**: `/magnificent-7/team/{team_id}`

**Description**: `GET` Request that returns the "Magnificent 7" team for a specific Premier League team.

**Path Parameter**:
- `team_id`: The ID of the Premier League team.

#### Example Request:
```bash
curl -X GET "http://localhost:8000/magnificent-7/team/1"
```

## Setup and Installation

### 1. CD to Repository

```bash
cd magnificent-7-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Testing the API

You can visit:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

You can also test the API using `curl` or Postman.

## Running Tests

To run unit tests:

```bash
pytest
```

## Future Enhancements

- **Improved endpoints**: Create endpoint that can search for a teams magnificent 7 using the team name. I would still keep ID based endpoint though.
- **Caching**: Caching to reduce API response time and minimize repeated API calls. Another natural progression of this idea would be database integration which I persoanlly would pivot to Django to achieve.
- **Project Improvement**: Containerise the project. Id first add devcontainers for local team development, Docker, and then Kubernetes if we are ultimately going to host this on the cloud.