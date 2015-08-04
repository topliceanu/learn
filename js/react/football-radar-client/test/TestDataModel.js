chai = require('chai')

DataModel = require('../app/lib/DataModel');


describe('DataModel', function () {

    describe('.sort()', function () {

        it('should correctly sort two teams by points', function () {
            var team1 = DataModel.factory();
            team1.id = 1;
            team1.name = 'Team1';
            team1.points = 10

            var team2 = DataModel.factory()
            team2.id = 2;
            team2.name = 'Team2';
            team2.points = 20

            var dm = new DataModel;
            dm.items = [team1, team2];
            dm.sort();

            chai.assert.lengthOf(dm.items, 2, 'should have both items');
            chai.assert.equal(dm.items[0].id, team2.id,
                'team2 has more points so it is first');
            chai.assert.equal(dm.items[1].id, team1.id,
                'team1 has less points so it is second');
        });

        it('should sort correctly sort two teams by goalDifference', function () {
            var team1 = DataModel.factory();
            team1.id = 1;
            team1.name = 'Team1';
            team1.points = 20;
            team1.goalDifference = 5;

            var team2 = DataModel.factory()
            team2.id = 2;
            team2.name = 'Team2';
            team2.points = 20;
            team2.goalDifference = 10;

            var dm = new DataModel;
            dm.items = [team1, team2];
            dm.sort();

            chai.assert.lengthOf(dm.items, 2, 'should have both items');
            chai.assert.equal(dm.items[0].id, team2.id,
                'team2 has higher goalDifference so it is first');
            chai.assert.equal(dm.items[1].id, team1.id,
                'team1 has smaller goalDifference so it is second');
        });

        it('should sort correctly sort two teams by goalsFor', function () {
            var team1 = DataModel.factory();
            team1.id = 1;
            team1.name = 'Team1';
            team1.points = 20;
            team1.goalDifference = 10;
            team1.goalsFor = 10;

            var team2 = DataModel.factory()
            team2.id = 2;
            team2.name = 'Team2';
            team2.points = 20;
            team2.goalDifference = 10;
            team2.goalsFor = 15;

            var dm = new DataModel;
            dm.items = [team1, team2];
            dm.sort();

            chai.assert.lengthOf(dm.items, 2, 'should have both items');
            chai.assert.equal(dm.items[0].id, team2.id,
                'team2 scored more goals so it is first');
            chai.assert.equal(dm.items[1].id, team1.id,
                'team1 scored less goals so it is second');
        });

        it('should sort correctly sort two teams by name', function () {
            var team1 = DataModel.factory();
            team1.id = 1;
            team1.name = 'Team10';
            team1.points = 20;
            team1.goalDifference = 10;
            team1.goalsFor = 10;

            var team2 = DataModel.factory()
            team2.id = 2;
            team2.name = 'Team1';
            team2.points = 20;
            team2.goalDifference = 10;
            team2.goalsFor = 10;

            var dm = new DataModel;
            dm.items = [team1, team2];
            dm.sort();

            chai.assert.lengthOf(dm.items, 2, 'should have both items');
            chai.assert.equal(dm.items[0].id, team2.id,
                'team2 goes first when sorting lexicographically');
            chai.assert.equal(dm.items[1].id, team1.id,
                'team5 goes second when sorting lexicographically');
        });
    });

    describe('.bootstrap()', function () {
        it('should initialize the data model with teams', function () {
            var dm = new DataModel();
            dm.bootstrap([{id: 1, name: 'Team10'}, {id: 2, name: 'Team1'}]);

            chai.assert.lengthOf(dm.items, 2,
                 'should have inserted the team objects');
            chai.assert.lengthOf(Object.keys(dm.dict), 2,
                 'should have store team object references in the dictionary');
            chai.assert.deepEqual(dm.items[0], dm.dict[2],
                'team1 is the first in the list because of its name');
            chai.assert.deepEqual(dm.items[1], dm.dict[1],
                'team10 is the second in the list after team10');
        });
    });

    describe('.update()', function () {

        it('should ignore update if at most one of the teams is unknown', function () {
            var dm = new DataModel;
            dm.bootstrap([{id: 1, name: 'Team1'}, {id: 2, name: 'Team2'}]);

            dm.update({
                date: "13/08/11",
                homeTeamId: 1,
                awayTeamId: 4,
                homeGoals: 1,
                awayGoals: 2
            });

            chai.assert.equal(dm.dict[1].played, 0, 'no updates processed');
            chai.assert.equal(dm.dict[2].played, 0, 'no updates processed');
        });

        it('should update the the data model after a game update', function () {
            var dm = new DataModel;
            dm.bootstrap([{id: 1, name: 'Team1'}, {id: 2, name: 'Team2'}]);

            dm.update({
                date: "13/08/11",
                homeTeamId: 1,
                awayTeamId: 2,
                homeGoals: 1,
                awayGoals: 2
            });

            chai.assert.equal(dm.dict[1].played, 1, 'one game played by Team1');
            chai.assert.equal(dm.dict[1].won, 0, 'Team2 won the game');
            chai.assert.equal(dm.dict[1].drawn, 0, 'Team2 won the game');
            chai.assert.equal(dm.dict[1].lost, 1, 'Team1 lost this game');
            chai.assert.equal(dm.dict[1].goalsFor, 1, 'Team1 scored 1 goal');
            chai.assert.equal(dm.dict[1].goalsAgainst, 2, 'Team1 received 2 goals');
            chai.assert.equal(dm.dict[1].goalDifference, -1, 'Team1 received one goal more then they scored');
            chai.assert.equal(dm.dict[1].points, 0, 'Team1 lost so no points');

            chai.assert.equal(dm.dict[2].played, 1, 'one game played by Team2');
            chai.assert.equal(dm.dict[2].won, 1, 'Team2 won the game');
            chai.assert.equal(dm.dict[2].drawn, 0, 'Team2 won the game');
            chai.assert.equal(dm.dict[2].lost, 0, 'Team2 won this game');
            chai.assert.equal(dm.dict[2].goalsFor, 2, 'Team2 scored 2 goals');
            chai.assert.equal(dm.dict[2].goalsAgainst, 1, 'Team2 received 1 goals');
            chai.assert.equal(dm.dict[2].goalDifference, 1, 'Team2 received one goal less then they scored');
            chai.assert.equal(dm.dict[2].points, 3, 'Team2 won so they get 3 points');

            // Test sorting algorithm.
            chai.assert.equal(dm.items[0].id, 2, 'Team2 is in the lead with 3 points');
        });

        it('should update the the data model after a draw game', function () {
            var dm = new DataModel;
            dm.bootstrap([{id: 1, name: 'Team1'}, {id: 2, name: 'Team2'}]);

            dm.update({
                date: "13/08/11",
                homeTeamId: 1,
                awayTeamId: 2,
                homeGoals: 1,
                awayGoals: 1
            });

            chai.assert.equal(dm.dict[1].played, 1, 'one game played by Team1');
            chai.assert.equal(dm.dict[1].won, 0, 'No team won the game');
            chai.assert.equal(dm.dict[1].drawn, 1, 'The game was a draw');
            chai.assert.equal(dm.dict[1].lost, 0, 'No team lost this game');
            chai.assert.equal(dm.dict[1].goalsFor, 1, 'Team1 scored 1 goal');
            chai.assert.equal(dm.dict[1].goalsAgainst, 1, 'Team1 received 1 goals');
            chai.assert.equal(dm.dict[1].goalDifference, 0, 'Team1 received as many goals as they scored');
            chai.assert.equal(dm.dict[1].points, 1, 'Team1 got 1 point for draw');

            chai.assert.equal(dm.dict[2].played, 1, 'one game played by Team2');
            chai.assert.equal(dm.dict[2].won, 0, 'Team2 won the game');
            chai.assert.equal(dm.dict[2].drawn, 1, 'Team2 won the game');
            chai.assert.equal(dm.dict[2].lost, 0, 'Team2 won this game');
            chai.assert.equal(dm.dict[2].goalsFor, 1, 'Team2 scored 1 goals');
            chai.assert.equal(dm.dict[2].goalsAgainst, 1, 'Team2 received 1 goals');
            chai.assert.equal(dm.dict[2].goalDifference, 0, 'Team2 received as many goals as they scored');
            chai.assert.equal(dm.dict[2].points, 1, 'Team2 got 1 point for draw');

            // Test sorting algorithm.
            chai.assert.equal(dm.items[0].id, 1, 'Team1 is first just because of the name');
        });
    });
});
