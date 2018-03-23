#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:13:35 2017

@author: Dovla
"""

db.dropDatabase()
db.collection.drop()
show dbs
show collections
use db

#Import csv
########################################

mongoimport -d test1 -c Users --type csv --file /Users/Dovla/Dropbox/Fax/DM/Users.csv --headerline
mongoimport -d test1 -c Posts --type csv --file /Users/Dovla/Dropbox/Fax/DM/Posts.csv --headerline

#SELECT,INSERT, UPDATE,DELETE
########################################
db.Users.findOne()

db.Users.insert({item: "card", qty: 15})
db.Users.find({"item":"card"})

db.Users.update({"item":"card"},{"item":"card","qty":20})
db.Users.update({"item":"card"},{$set:{qty:20}})
db.Users.find({"item":"card"})

db.Users.deleteOne({"item":"card"})
db.Users.find({"item":"card"})

#WHERE
########################################
db.Users.find({"Views":{$gt:30000}}).pretty()
#AND
########################################
db.Users.find({$and:[{"Views":{$gt:30000}},{"DownVotes":{$lt:500}}]}).pretty()

########################################
#WHERE AND SUM
db.Users.aggregate({$match:{"Views":{$gt:30000}}}, {$count:"Views"})


########################################
#Buckets
db.Users.aggregate([{$bucket:{groupBy: "$Views",boundaries: [0,20,50,100,300,500,1000,5000],default:"Other",output:{"count":{$sum:1}}}},{$out:"Bucket1"}])
> db.Bucket1.find({})

db.Users.aggregate([{$bucket:{groupBy: "$Views",boundaries: [0,20,50,100,300,500,1000,5000],default:"Other",output:{"count":{$sum:1}, "Users":{$push:"$DisplayName"}}}},{$out:"Bucket1"}])
> db.Bucket1.findOne()


########################################
#FOR EACH - JS
db.Users.find({"Views":{$gt:30000}}).forEach(function(doc){
    db.Users.update({_id: doc._id},{$set:{"Age": 25000}});
})
db.Users.find({"Views":{$gt:30000}}).pretty()

########################################
#Joins
db.Posts10k.aggregate([{$lookup:{from: "Users10k",localField: "AccountId",foreignField: "OwnerUserId",as: "Users1"}}]).pretty()
db.Posts.aggregate([{$lookup:{from: "Users",localField: "AccountId",foreignField: "OwnerUserId",as: "Users"}}, {$out:"Joins123"}])

> db.Posts10k.aggregate([{$lookup:{from: "Users10k",localField: "AccountId",foreignField: "OwnerUserId",as:"Users1"}},{$out:"impJoin6"}])
db.try1.aggregate([{$lookup:{from: "Posts",localField: "OwnerUserId",foreignField: "AccountId",as: "Posts"}},{"$out": "some"}])

db.Users.aggregate([{$lookup:{from: "Posts",localField: "OwnerUserId",foreignField: "Id",as: "Posts"}}, {$project:{Posts: {$filter:{input:"$Posts",as: "Posts", cond: {$ne:[]}}}]).pretty()


db.orders.insert({ "_id" : 1, "item" : "abc", "price" : 12, "quantity" : 2 })
db.orders.insert({ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1 })
db.orders.insert({ "_id" : 3  })

db.inventory.insert({ "_id" : 1, "sku" : "abc", description: "product 1", "instock" : 120 })
db.inventory.insert({ "_id" : 2, "sku" : "def", description: "product 2", "instock" : 80 })
db.inventory.insert({ "_id" : 3, "sku" : "ijk", description: "product 3", "instock" : 60 })
db.inventory.insert({ "_id" : 4, "sku" : "jkl", description: "product 4", "instock" : 70 })
db.inventory.insert({ "_id" : 5, "sku": null, description: "Incomplete" })
db.inventory.insert({ "_id" : 6 })

db.orders.aggregate([{$lookup:{from: "inventory", localField: "item",foreignField: "sku",as: "inventory_docs"}}, {$out:"joinedTrue"}])


########################################
#MAP REDUCE

var mapFunction1 = function() {
                       emit(this.OwnerUserId, this.Score);
                   };
var reduceFunction1 = function(keyOwnerUserId, valuesScore) {
                          return Array.sum(valuesScore);
                      };

db.Posts.mapReduce(
                     mapFunction1,
                     reduceFunction1,
                     { out: "map_reduce_example2" }
                   )
        


















db.orders.insert({
     _id: ObjectId("50a8240b927d5d8b5891741c"),
     cust_id: "abc123",
     ord_date: new Date("Oct 04, 2012"),
     status: 'A',
     price: 20,
     items: [ { sku: "mmm", qty: 5, price: 2 },
              { sku: "nnn", qty: 5, price: 2 } ]
})

db.orders.insert({
     _id: ObjectId("50a8240b927d5d8b5891742c"),
     cust_id: "abc1234",
     ord_date: new Date("Oct 04, 2012"),
     status: 'A',
     price: 25,
     items: [ { sku: "mmm", qty: 5, price: 2.5 },
              { sku: "nnn", qty: 5, price: 2.5 } ]
})

db.orders.insert({
     _id: ObjectId("50a8240b927d5d8b5891744c"),
     cust_id: "abc125",
     ord_date: new Date("Oct 04, 2012"),
     status: 'A',
     price: 30,
     items: [ { sku: "mmm", qty: 5, price: 3 },
              { sku: "nnn", qty: 5, price: 3 } ]
})


db.orders.insert({
     _id: ObjectId("50a8240b927d5d8b5891745c"),
     cust_id: "abc125",
     ord_date: new Date("Oct 04, 2012"),
     status: 'A',
     price: 30,
     items: [ { sku: "mmm", qty: 5, price: 3 },
              { sku: "nnn", qty: 5, price: 3 } ]
})


var mapFunction1 = function() {
                       emit(this.cust_id, this.price);
                   };


var reduceFunction1 = function(keyCustId, valuesPrices) {
                          return Array.sum(valuesPrices);
                      };

db.orders.mapReduce(
                     mapFunction1,
                     reduceFunction1,
                     { out: "map_reduce_example" }
                   )


########################################
Operator near
{
   <location field>: {
     $near: {
       $geometry: {
          type: "Point" ,
          coordinates: [ <longitude> , <latitude> ]
       },
       $maxDistance: <distance in meters>,
       $minDistance: <distance in meters>
     }
   }
}

Create Views


