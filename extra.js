function getData(){
  ajaxGetRequest('bar',showBar)
  ajaxGetRequest('pie',showPie)
}

function showBar(response){
  let data= JSON.parse(response);
  let x1=[];
  let y1=[];
  for (let line of data){
    x1.push(line['location'])
    y1.push(line['series_complete_pop_pct'])
  }
  let barData = [{
    x: x1,
    y: y1,
    type:'bar'
  }];
  let layout= {
    title: "Fully Vaccinated by Location",
    xaxis:{
      title: "Location"
    },
    yaxis: {
      title: "% Fully Vaccinated"
    }
  }
Plotly.newPlot('bar', barData,layout);
}

function showPie(response){
  let out=[];
  let data=JSON.parse(response);
  let jan=0;
  let mod=0;
  let pfi=0;
  let oth=0;
  for (let line of data){
    jan+=Number(line['administered_janssen']);
    mod+=Number(line['administered_moderna']);
    pfi+=Number(line['administered_pfizer']);
    oth+=Number(line['administered_unk_manuf']);
  }
  out.push(jan);
  out.push(mod);
  out.push(pfi);
  out.push(oth);
  let dataFinal = [{
  values: out,
  labels: ['Janssen','Moderna','Pfizer','Other'],
  type: 'pie'
}];

var layout = {
  title: "Vaccine Manufacturer Market Share",
  height: 400,
  width: 500
};

Plotly.newPlot('pie', dataFinal, layout);
}


function showLine(response){
  let temp=document.getElementById('locText').value
  let data=JSON.parse(response);
  let x1=[]
  let y1=[]
  for (let line of data){
    x1.push(line['date'])
    y1.push(line['series_complete_pop_pct'])
  }

  let trace1 = {
  x: x1,
  y: y1,
  type: 'line'
};
out=[trace1]
let layout = {
  title:'% of '+temp+" Fully Vaccinated by Date",
  xaxis: {title:'Date'},
  yaxis: {title:'% Fully Vaccinated'}
};

Plotly.newPlot('line', out,layout);
}

function getLocData(){
  let x=document.getElementById('locText');
  let y=x['value']
  let yo=JSON.stringify(y)
  ajaxPostRequest('/line',yo,showLine)
}