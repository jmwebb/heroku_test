counter = 0;

(function() {
	request();
})();

function request() {
	$.ajax({
		url: "/test/", 
		success: function(result){
			counter += 1;
        	console.log("Counter " + counter);
        	request();
    	}
	});
}