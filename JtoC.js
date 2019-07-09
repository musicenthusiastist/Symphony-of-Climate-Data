let fs = require('fs')   
let file = "d:\\AHCCD_hist_annual_ON_6010735_TMEAN_P1Y.json"   
fs.readFile(file, function(err, data) {
  if (err) {
	console.log("Read File Error.\nCheck Json File at " + file)
  } else {
	let source = JSON.parse(data)
	let str = "Year,MeanTemp\n"
	for (i = 0; i <source.features.length; i++) 
		str = str + source.features[i].properties.year + "," + source.features[i].properties.value + "\n"  // parsing data
	let toFile = "d:\\result.csv"
	fs.writeFile(toFile, str,function(err, data) {
	  if (err) {
		console.log("Write File Error! Please Close " + toFile)
	  } else {
		console.log("Wrote File at "+ toFile)
	  }
	})
  }
})



 