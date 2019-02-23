"use strict";

window.momentum = window.momentum || {};



momentum.Core = function() {
  this.timeStr = "";
  this.quoteStr = "";
  this.weatherStr = "";
  this.ampm = "AM";
  this.salutation = "morning";
  this.location = "";
  
  this.timeEl = $("#time");
  this.quoteEl = $("#quote-text");
  this.weatherEl = $("#weather");
  this.greetingEl = $("#greetings");
  this.ampmEl = $("#ampm");
  this.city = $("#location");
  this.lat;
  this.lon;
  
  this.weatherCtrl = new momentum.WeatherCtrl();
  
  
  this.quoteCtrl = new momentum.QuoteCtrl();
};

momentum.Core.prototype = {
	
  setTime: function() {
		var date = new Date();
		var hours = date.getHours();
		if(hours>12){
			this.salutation = "afternoon";
		}
		if(hours>18){
			this.salutation = "evening";
		}
		if(hours > 11 && hours < 24){
			this.ampm = "PM";
		}
		if(hours > 12){
			hours -= 12;
		}
		var mins = date.getMinutes();
		if(mins < 10){
			var txt = '0' + mins;
			mins = txt; 
		}
		var ret = '';
		ret = ret + hours + ':' + mins;
		this.timeStr = ret;
  },
	  setQuote: function(quoteData) {
		this.quoteStr = quoteData.message;
		this.quoteEl.text(this.quoteStr);
		this.render();
  },
  setWeather: function(weatherData) {
		
		this.weatherStr = Math.floor(weatherData.main.temp - 273.15);
		this.location = weatherData.name;
		this.render();
  },
 updateTime: function() {
		
		this.setTime();
  },
  updateWeather: function() {
	
	this.weatherCtrl.fetchWeather(this.lat, this.lon, this.setWeather.bind(this));
  },
	updateQuote: function() {
		
		this.quoteCtrl.fetchQuote(this.setQuote.bind(this));

	},
	start: function() {
			if (!navigator.geolocation){
		  throw "Geolocation not supported!";
		}

		function error() {
		  throw "Error occured!";
		};

		navigator.geolocation.getCurrentPosition(function(position) {
		  console.log("EXECUTING");
		  this.lat = position.coords.latitude;
		  this.lon = position.coords.longitude;
		  console.log(this.lat, this.lon);
		  this.updateWeather();
		}.bind(this), error);
		this.setTime();
		
		this.updateQuote();
		this.render();

		
		

	},
  render: function() {
		
		this.timeEl.text(this.timeStr);
		this.greetingEl.text("Good " + this.salutation +", Ying Hang");
		this.ampmEl.text(this.ampm);
		this.weatherEl.text(this.weatherStr);
		this.quoteEl.text(this.quoteStr);
		this.city.text(this.location);
  }
};