// Check that modules can be resolved, given a list of module names as args
var x;

process.argv.slice(2).forEach(function(val, index, array) {

	try {
		console.log(val + ':' + require.resolve(val));
	}
	catch(e){
		console.log(val + ':' + 'not found');
	}
}) 