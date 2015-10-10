# Football Radar - JavaScript Task

_Realtime league table task_

## Introduction

As part of your application to Football Radar, we would like you to complete a small task similar to the kind of thing you could end up working on here. The purpose of this task is to evaluate your skill in building effective user interfaces, integrating with a variety of upstream sources.

For this task, we would like you to generate a realtime league table from games published over a WebSocket connection. We have provided a basic WebSocket and HTTP server to provide you with all the data you will need.

The games in this task are taken from the 2011/12 English Premier League season. For reference, the final table is available here: http://en.wikipedia.org/wiki/2011-12_Premier_League#League_table.

## Getting started

You will first need to get the server running. Ensure that you have installed the relevant dependencies and then start the server via `npm start`. By default, the server will be available at http://localhost:8080.

There are two data sources that you will need to work with:

### Teams

A list of teams for the season is available at http://localhost:8080/teams. This is a regular HTTP endpoint that returns a list of teams as JSON. The format of the response is as follows:

```json
[
    { "id": 1, "Blackburn" },
    { "id": 2, "Wolves" }
]
```

### Games

A stream of games is available at http://localhost:8080/games. This is a realtime stream over WebSockets that you will need to consume. The format of each message is as follows:

```json
{
    "date": "13/08/11",
    "homeTeamId": 1,
    "awayTeamId": 2,
    "homeGoals": 1,
    "awayGoals": 2
}
```

## Rules

* The league table should comprise 20 teams, each starting with 0 points.
* Upon consuming a new game over the WebSocket stream, the league table must be updated.
* 3 points are awarded for a win, 1 for a draw and 0 for a loss
* Teams must be ordered with respect to the following: points, goal difference, goals for and finally team name.

## Your solution

Please ensure that you include all relevant build steps and tests when submitting your solution, as we will take these into account when considering your application. Your solution only needs to work on modern browsers. We will test against the latest release of Google Chrome unless you specify otherwise.
