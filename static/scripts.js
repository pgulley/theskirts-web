function get_doodl(i){
	return `<div id="doodl${ i }"></div>`
}

//instead of 30 sequential, 
//a larger number of randomly selected from a range of 30. 
//math.random()
$(document).ready(function(){
	for(i=0;i<100;i++){
		$(".doodls").append(get_doodl(Math.floor((Math.random() * 40))))
	}
})