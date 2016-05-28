// Data structure to store all application information.
// The data for each team is stored in an plain object. All objects are stored
// in an array, which is sorted given special rules (see .sort()). Also
// for fast retrieval of a team by it's id, team objects are also linked to a
// dictionary where the keys are ids.
var DataModel = function () {
    // Format of this.items is:
    // [
    //      {
    //          id:number,
    //          name:string,
    //          played:number,
    //          won:number,
    //          drawn:number,
    //          lost:number,
    //          goalsFor:number,
    //          goalsAgainst:number,
    //          goalDifference:number,
    //          points:number
    //      }
    // ]
    this.items = [];
    // Stores pointers to each object in the data array indexed by team id.
    // Format of this.dict is: {id: teamObject}
    this.dict = {};
};


// Initialize the data model given a list of team names and ids.
//
// @param {Array} items
// @param {Number} items[k].id - id of the team.
// @param {String} items[k].name - name of the team.
DataModel.prototype.bootstrap = function (items) {
    var that = this;
    items.forEach(function (item) {
        var newItem = DataModel.factory();
        newItem.id = item.id
        newItem.name = item.name

        that.dict[item.id] = newItem;
        that.items.push(newItem);
    });
    this.sort();
};


// Sorts the encapsulated data maintaining these rules:
//
// 1. sort by points first.
// 2. sort by goalDifference for teams with equal points.
// 3. sort by goalsFor for teams with equal points and goalDifference.
// 4. sort by name for teams with equal points, goalDifference and goalsFor.
DataModel.prototype.sort = function () {
    var compare = function (a, b) {
        if (a.points > b.points)
            return -1
        if (a.points < b.points)
            return 1

        if (a.goalDifference > b.goalDifference)
            return -1
        if (a.goalDifference < b.goalDifference)
            return 1

        if (a.goalsFor > b.goalsFor)
            return -1
        if (a.goalsFor < b.goalsFor)
            return 1

        if (a.name > b.name)
            return 1
        if (a.name < b.name)
            return -1

        return 0
    };
    this.items.sort(compare);
};


// Insert a new update into the data model handling the following cases:
// 1. if the team is not yet in the data object, it has to be inserted with
//    default values
// 2. if the team exists in the data model, it has to be updated accordingly.
// 3. maintain this.dict dictionary of references.
// 4. maintain the sorted order of the list.
//
// Note! This is the most important method of the application!
//
// @param {Object} news - an update object
// @param {String} news.date - when the update occured. Ignored!
// @param {Number} news.homeTeamId - id of the host team.
// @param {Number} news.awayTeamId - id of the guest team.
// @param {Number} news.homeGoals - number of goals scored by the host team.
// @param {Number} news.awayGoals - number of goals scored by the guest team.
//
DataModel.prototype.update = function (news) {
    var homeTeam = this.dict[news.homeTeamId];
    var awayTeam = this.dict[news.awayTeamId];

    if (homeTeam == null) {
        console.error('Update ignored because team with id '+news.homeTeamId+' is not known');
        return;
    }
    if (awayTeam == null) {
        console.error('Update ignored because team with id '+news.awayTeamId+' is not known');
        return;
    }

    // both teams played a new game.
    homeTeam.played += 1;
    awayTeam.played += 1;

    // winning team gets 3 points, losing team gets 0 points, on draw, both
    // teams get 1 point.
    if (news.homeGoals > news.awayGoals) { // home team won!
        homeTeam.won += 1
        awayTeam.lost += 1
        homeTeam.points += 3
    }
    else if (news.homeGoals < news.awayGoals) { // away team won!
        homeTeam.lost += 1
        awayTeam.won += 1
        awayTeam.points += 3
    }
    else { // draw!
        homeTeam.drawn += 1
        awayTeam.drawn += 1
        homeTeam.points += 1
        awayTeam.points += 1
    }

    homeTeam.goalsFor += news.homeGoals;
    awayTeam.goalsFor += news.awayGoals;

    homeTeam.goalsAgainst += news.awayGoals;
    awayTeam.goalsAgainst += news.homeGoals;

    homeTeam.goalDifference += news.homeGoals - news.awayGoals;
    awayTeam.goalDifference += news.awayGoals - news.homeGoals;

    // sort the data list after these updates.
    this.sort();
};


// Helper static method to build an initial raw team object.
DataModel.factory = function () {
    return {
        id: null,
        name: null,
        played: 0,
        won: 0,
        drawn: 0,
        lost: 0,
        goalsFor: 0,
        goalsAgainst: 0,
        goalDifference: 0,
        points: 0
    };
};


module.exports = DataModel;
