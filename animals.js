"use strict";

//This is the on load functions
//Pie Chart: Amount of Total Animals Per Year
function apy(response) {
  let resp = JSON.parse(response);
  console.log(resp)
  let data = [{
  values: resp,
  labels: ['2011', '2012', '2013'],
  type: 'pie'
  }];
  let layout = {
  title: 'Amount of Total Animals Admitted per Year',
  height: 400,
  width: 500
  };
Plotly.newPlot('amt', data, layout);
}
//Table: Amount of Animals Admitted in a Los Angeles Shelter per a Given Year
function tablepy(response){
  let resp = JSON.parse(response);
  console.log(resp)
  let values = [
      ['E & W VALLEY', 'S & W LA', 'HARBOR', 'N CENTRA'],
      resp[0],
      resp[1],
      resp[2]]

  let data = [{
    type: 'table',
    columnwidth: [45, 25],
    header: {
      values: [["<b>Shelters</b>"], ["<b>2011</b>"],
          ["<b>2012</b>"], ["<b>2013</b>"]],
      align: "center",
      line: {width: 2, color: 'black'},
      fill: {color: "#165fcc50"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: values,
      align: "center",
      height: 30,
      line: {color: "black", width: 2},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]
  Plotly.plot('graph', data);
}

function getData() {
  ajaxGetRequest("/AnimalsPerYear", apy);
  ajaxGetRequest("/table", tablepy);
}
/////////////////////////////////////////////////
//Pie Chart: Amount of DOGS per year
function dogpy(response) {
  let resp = JSON.parse(response);
  console.log(resp)
  let data = [{
  values: resp,
  labels: ['2011', '2012', '2013'],
  type: 'pie'
  }];
  let layout = {
  title: 'Amount of Dogs Admitted per Year',
  height: 400,
  width: 500
  };
Plotly.newPlot('dog', data, layout);
}
//POST REQUEST
function dogpost(){
  let dogElement = document.getElementById("dbutton");
  let dogGraph = dogElement.value;
  dogElement.value = "";
  let toSend = JSON.stringify({"dbutton": dbutton });

  ajaxPostRequest('/dogPie', toSend, dogpy);
}
///////////////////////////////////////////////
//Pie Chart: Amount of CATS per year
function catpy(response) {
  let resp = JSON.parse(response);
  console.log(resp)
  let data = [{
  values: resp,
  labels: ['2011', '2012', '2013'],
  type: 'pie'
  }];
  let layout = {
  title: 'Amount of Cats Admitted per Year',
  height: 400,
  width: 500
  };
Plotly.newPlot('cat', data, layout);
}
//POST REQUEST
function catpost(){
  let catElement = document.getElementById("cbutton");
  let catGraph = catElement.value;
  catElement.value = "";
  let toSend = JSON.stringify({"cbutton": cbutton });

  ajaxPostRequest('/catPie', toSend, catpy);
}
///////////////////////////////////////////////
//Pie Chart: Amount of BIRDS per year
function birdpy(response) {
  let resp = JSON.parse(response);
  console.log(resp)
  let data = [{
  values: resp,
  labels: ['2011', '2012', '2013'],
  type: 'pie'
  }];
  let layout = {
  title: 'Amount of Birds Admitted per Year',
  height: 400,
  width: 500
  };
Plotly.newPlot('bird', data, layout);
}
//POST REQUEST
function birdpost(){
  let birdElement = document.getElementById("bbutton");
  let birdGraph = birdElement.value;
  birdElement.value = "";
  let toSend = JSON.stringify({"bbutton": bbutton });

  ajaxPostRequest('/birdPie', toSend, birdpy);
}
////////////////////////////////////////////////// 
//Pie Chart: Amount of Wildlife per year
function otherpy(response) {
  let resp = JSON.parse(response);
  console.log(resp)
  let data = [{
  values: resp,
  labels: ['2011', '2012', '2013'],
  type: 'pie'
  }];
  let layout = {
  title: 'Amount of Wildlife Admitted per Year',
  height: 400,
  width: 500
  };
Plotly.newPlot('other', data, layout);
}
//POST REQUEST
function otherpost(){
  let otherElement = document.getElementById("obutton");
  let otherGraph = otherElement.value;
  otherElement.value = "";
  let toSend = JSON.stringify({"obutton": obutton });

  ajaxPostRequest('/otherPie', toSend, otherpy);
}

/////////////////////////////////////////////////

//Table: Amount of animals admitted in an LA Shelter in 2011
function tableData11(response){
  let resp = JSON.parse(response);
  console.log(resp)
  let values = [
      ['E & W VALLEY', 'S & W LA', 'HARBOR', 'N CENTRA'],
      resp[0]]

  let data = [{
    type: 'table',
    columnwidth: [45, 25],
    header: {
      values: [["<b>Shelters</b>"], ["<b>2011</b>"]],
      align: "center",
      line: {width: 2, color: 'black'},
      fill: {color: "#165fcc50"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: values,
      align: "center",
      height: 30,
      line: {color: "black", width: 2},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]
  Plotly.plot('2011graph', data);
}
//POST REQUEST
function table11(){
  let otherElement = document.getElementById("button11");
  let otherGraph = otherElement.value;
  otherElement.value = "";
  let toSend = JSON.stringify({"button11": button11 });

  ajaxPostRequest('/t11', toSend, tableData11);
}
/////////////////////////////////////////////////////
//Table: Amount of animals admitted in an LA Shelter in 2012
function tableData12(response){
  let resp = JSON.parse(response);
  console.log(resp)
  let values = [
      ['E & W VALLEY', 'S & W LA', 'HARBOR', 'N CENTRA'],
      resp[1]]

  let data = [{
    type: 'table',
    columnwidth: [45, 25],
    header: {
      values: [["<b>Shelters</b>"],
          ["<b>2012</b>"]],
      align: "center",
      line: {width: 2, color: 'black'},
      fill: {color: "#b3daff"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: values,
      align: "center",
      height: 30,
      line: {color: "black", width: 2},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]
  Plotly.plot('2012graph', data);
}
//POST REQUEST
function table12(){
  let otherElement = document.getElementById("button12");
  let otherGraph = otherElement.value;
  otherElement.value = "";
  let toSend = JSON.stringify({"button12": button12 });

  ajaxPostRequest('/t12', toSend, tableData12);
}
////////////////////////////////////////
//Table: Amount of animals admitted in an LA Shelter in 2013
function tableData13(response){
  let resp = JSON.parse(response);
  console.log(resp)
  let values = [
      ['E & W VALLEY', 'S & W LA', 'HARBOR', 'N CENTRA'],
      resp[2]]

  let data = [{
    type: 'table',
    columnwidth: [45, 25],
    header: {
      values: [["<b>Shelters</b>"],
          ["<b>2013</b>"]],
      align: "center",
      line: {width: 2, color: 'black'},
      fill: {color: "#cce6ff"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: values,
      align: "center",
      height: 30,
      line: {color: "black", width: 2},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]
  Plotly.plot('2013graph', data);
}
//POST REQUEST
function table13(){
  let otherElement = document.getElementById("button13");
  let otherGraph = otherElement.value;
  otherElement.value = "";
  let toSend = JSON.stringify({"button13": button13 });

  ajaxPostRequest('/t13', toSend, tableData13);
}

////////////////////////////////////////////////////
//AJAX POST and GET Requests
function ajaxGetRequest(path, callback) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState===4 && this.status ===200) {
      callback(this.response);
    }
  }
  request.open("GET", path);
  request.send();
}

function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
      if (this.readyState===4&&this.status ===200){
          callback(this.response);
      }
  };
  request.open("POST", path);
  request.send(data);
}