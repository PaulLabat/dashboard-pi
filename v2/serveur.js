var mongoose = require('mongoose');
var socket = require('socket.io');
var addrmongo = "mongodb://localhost:27017/test";

mongoose.connect(addrmongo, function(err) {
    if (err) {
        throw err;
    }else{
        console.log("success");
    }
});
/*
MongoDB
*/

var nouritureDansLeFrigoSchema = mongoose.Schema({
    nom: String, 
    quantite: String,
},{
    collection: nouritureDansLeFrigo                                     
});

var nouritureDansLeFrigoChoixSchema = mongoose.Schema({
    nom: String, 
    quantite: String,
},{
    collection: nouritureDansLeFrigoChoix                                     
});
var nouritureDansLeFrigo = mongoose.model('nouritureDansLeFrigo', nouritureDansLeFrigoSchema);
var nouritureDansLeFrigoChoix = mongoose.model('nouritureDansLeFrigoChoix', nouritureDansLeFrigoChoixSchema);


var io = socket.listen(3000);
io.set('log level', 0);


io.sockets.on('connection', function(socket){
    socket.on('getchoix', function(){
        console.log('getchoix');
        nouritureDansLeFrigoChoix.find().exec(function(err, doc){
            if(err){
                console.log('error find choix');
            }else{
                var res = JSON.parse(JSON.stringify(doc));
                socket.emit('getchoix', res);
            }
        });


    });

    socket.on('insertIntoFrigo', function(nom, quantite){
        console.log('insertintofrigo', nom, quantite); 
        var newEntry = new nouritureDansLeFrigo({
            nom:nom,
            quantite:quantite
        });

        newEntry.save(function(err, doc){
            if(err)return console.error(err);
            else{
                var json = [{_id:doc.id,nom:nom, quantite:quantite}];
                socket.emit('getDansLeFrigo', json);
            }
        });


    });

    socket.on('getDansLeFrigo', function(){
        console.log('getdanslefrigo');

        nouritureDansLeFrigo.find().exec(function(err, doc){
            if(err) console.log('error find liste dans le frigo');
            else{
                var res = JSON.parse(JSON.stringify(doc));
                socket.emit('getDansLeFrigo', res);
            }

        });

    });

    socket.on('removeElementFromFrigo', function(elem){
        nouritureDansLeFrigo.findByIdAndRemove(elem, function(err, res){
        if(err){
            console.log('error removing from database');
        }else{
            console.log('success removing from database');
        }
        
        });
    });




});





/*var newChoix = new nouritureDansLeFrigoChoix({
    nom:"steak",
    quantite: 5

});


newChoix.save(function(err, newChoix){
    if(err) return console.error(err);
    else console.log("success save");
});*/