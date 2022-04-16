var ticksStyle = {
	fontColor: '#495057',
	fontStyle: 'bold',
	stepSize: 5,
}

var mode = 'index'
var intersect = true
var profitHistory;
var botsGlobal = [];

function updateProfitHistoryChart(chartData) {
	var labelList = [];
	var profitData = [];
	for (let i = 0; i < chartData.length; i++) {
		timestamp = moment.unix(chartData[i].timestamp).format("YYYY-MM-DD hh:mm:ss")
		labelList.push(timestamp)
		profitData.push(chartData[i].profit)
	}
	console.log(profitData)

	var $profitHistoryChart = $('#profit-history-bot')
	if (profitHistory) {
		profitHistory.destroy();
	}
	profitHistory = new Chart($profitHistoryChart, {
		type: 'line',
		data: {
			labels: labelList,
			datasets: [{
				type: 'line',
				pointRadius: 1,
				label: 'Profit',
				data: profitData,
				borderColor: 'rgb(75, 192, 192)',
				borderWidth: 1,
				fill: false,
			    tension: 0.1
			}]
		},
		options: {
			maintainAspectRatio: false,
			tooltips: {
				mode: mode,
				intersect: intersect
			},
			hover: {
				mode: mode,
				intersect: intersect
			},
			scales: {
				yAxes: [{
					gridLines: {
						display: true,
						lineWidth: '4px',
						color: 'rgba(0, 0, 0, .2)',
						zeroLineColor: 'transparent'
					},
					ticks: $.extend({
						beginAtZero: true,
						suggestedMax: 100
					}, ticksStyle)
				}],
				xAxes: [{
					type: 'time',
					time: {
						unit: 'day',
						displayFormats: {
							'second': 'MM SS',
							'minute': 'hh:mm',
							'hour': 'DD hh',
							'day': 'MMM DD',
							'week': 'MMM DD',
							'month': 'MMM DD',
							'quarter': 'MMM DD',
							'year': 'MMM DD',
						  }
					},
					ticks: {
						// Include a dollar sign in the ticks
						callback: function(val, index) {
							// Hide the label of every 2nd dataset
							return index % 3 === 0 ? val : '';
						},
					}
				}]
			}
		}
	})
}

function loadProfitHistoryBotByTime(bot_id) {
	const csrftoken = Cookies.get('csrftoken');
	$.ajax({
		url: window.location.origin +
			"/api/profithistorybot/" + "?bot=" + bot_id,
		dataType: 'json',
		contentType: 'application/json',
		data: {},
		beforeSend: function (){
            showLoading(true, 1);
        },
        complete: function (){
            showLoading(false, 1);
        },
		success: function(response) {
			results = response['results']
			console.log(results)
			if(results.length > 0){
				updateProfitHistoryChart(results)
			}
		},
		error: function(response) {
			console.log("phongtran0715| Error: " + response);
		}
	});
}

function loadVolatilityBotByTime() {
	const csrftoken = Cookies.get('csrftoken');
	$.ajax({
		url: window.location.origin +
			"/api/volatilitybot/",
		dataType: 'json',
		contentType: 'application/json',
		data: {},
		success: function(response) {
			results = response['results']
			if(results.length > 0){
				initDropdowns(results)
			}
		},
		error: function(response) {
			console.log("phongtran0715| Error: " + response);
		}
	});
}

function initDropdowns(bots) {
    var dropdownMenuBot = document.getElementById("dropdownMenuBot")
	var dropdownBot = document.getElementById("dropdownBot")
	botsGlobal = bots
	dropdownBot.textContent = bots[0].name
	loadProfitHistoryBotByTime(bots[0].id)
	for (let i = 0; i < bots.length; i++) {
		dropdownMenuBot.innerHTML += `<button class="dropdown-item" href="#" type="button" onclick="onChangeDropdowns(${i})">${bots[i].name}</button>`;
	}
}

function onChangeDropdowns(i){
	var dropdownBot = document.getElementById("dropdownBot")
	dropdownBot.textContent = botsGlobal[i].name
	loadProfitHistoryBotByTime(botsGlobal[i].id)
}

function showLoading(show, spinner) {
    var spinnerOne = document.getElementById("spinner-one")
    if  (spinner === 1) {
        if (show === true) {
            spinnerOne.style.display = "flex"
        } else {
            spinnerOne.style.display = "none"
        }
    } else {
        if (show === true) {
            spinnerTwo.style.display = "flex"
        } else {
            spinnerTwo.style.display = "none"
        }
    }
}