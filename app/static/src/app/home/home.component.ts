import { Component, OnInit,OnDestroy } from '@angular/core';
import {TimerObservable} from "rxjs/observable/TimerObservable";
import {Subscription} from "rxjs/Subscription";
import {HomeService} from "./home.service";


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [HomeService]
})
export class HomeComponent implements OnInit, OnDestroy {
  responseData : any;

  data: any = {};
  private alive: boolean;
  private interval: number;
  isDataAvailable=false

  constructor(private homeService: HomeService) {
    this.alive = true;
    this.interval = 60000;
  }

  ngOnInit() {
    TimerObservable.create(0, this.interval)
      .takeWhile(() => this.alive)
      .subscribe(() => {
        this.homeService.get()
          .subscribe((data) => {
            this.data = data;
            this.transitPeriodchartData = [
              {data:[this.data.transit_period.in_5_min.mean,this.data.transit_period.in_15_min.mean,this.data.transit_period.in_60_min.mean], label:'Mean Time'},
              {data:[this.data.transit_period.in_5_min.median,this.data.transit_period.in_15_min.median,this.data.transit_period.in_60_min.median], label:'Median Time'},
              {data:[this.data.transit_period.in_5_min.percentile,this.data.transit_period.in_15_min.percentile,this.data.transit_period.in_60_min.percentile], label:'Percentile 95th'},
            ];
            this.securityPeriodchartData = [
              {data:[this.data.security_period.in_5_min.mean,this.data.security_period.in_15_min.mean,this.data.security_period.in_60_min.mean], label:'Mean Time'},
              {data:[this.data.security_period.in_5_min.median,this.data.security_period.in_15_min.median,this.data.security_period.in_60_min.median], label:'Median Time'},
              {data:[this.data.security_period.in_5_min.percentile,this.data.security_period.in_15_min.percentile,this.data.security_period.in_60_min.percentile], label:'Percentile 95th'},
            ];


            this.securityPeriodTableData5Min = [
              {
                data: [
                  this.data.security_period.in_5_min.mean,
                  this.data.security_period.in_5_min.median,
                  this.data.security_period.in_5_min.percentile
                ]
              }];


            this.securityPeriodchartData5Min = [
              {
                data: [
                  this.data.security_period.in_5_min.mean,
                  this.data.security_period.in_5_min.median
                ]
              }];

            this.securityPeriodTableData15Min = [
              {
                data: [
                  this.data.security_period.in_15_min.mean,
                  this.data.security_period.in_15_min.median,
                  this.data.security_period.in_15_min.percentile
                ]
              }];

            this.securityPeriodchartData15Min = [
              {
                data: [
                  this.data.security_period.in_15_min.mean,
                  this.data.security_period.in_15_min.median
                ]
              }];

            this.securityPeriodTableData60Min = [
              {
                data: [
                  this.data.security_period.in_60_min.mean,
                  this.data.security_period.in_60_min.median,
                  this.data.security_period.in_60_min.percentile
                ]
              }];



            this.securityPeriodchartData60Min = [
              {
                data: [
                  this.data.security_period.in_60_min.mean,
                  this.data.security_period.in_60_min.median
                ]
              }];


            this.transitPeriodTableData5Min = [
              {
                data: [
                  this.data.transit_period.in_5_min.mean,
                  this.data.transit_period.in_5_min.median,
                  this.data.transit_period.in_5_min.percentile
                ]
              }];


            this.transitPeriodchartData5Min = [
              {
                data: [
                  this.data.transit_period.in_5_min.mean,
                  this.data.transit_period.in_5_min.median
                ]
              }];

            this.transitPeriodTableData15Min = [
              {
                data: [
                  this.data.transit_period.in_15_min.mean,
                  this.data.transit_period.in_15_min.median,
                  this.data.transit_period.in_15_min.percentile
                ]
              }];


            this.transitPeriodchartData15Min = [
              {
                data: [
                  this.data.transit_period.in_15_min.mean,
                  this.data.transit_period.in_15_min.median
                ]
              }];

            this.transitPeriodTableData60Min = [
              {
                data: [
                  this.data.transit_period.in_60_min.mean,
                  this.data.transit_period.in_60_min.median,
                  this.data.transit_period.in_60_min.percentile
                ]
              }];


            this.transitPeriodchartData60Min = [
              {
                data: [
                  this.data.transit_period.in_60_min.mean,
                  this.data.transit_period.in_60_min.median
                ]
              }];


            this.transitPeriodchartDeviceData = [
                this.data.transit_period.in_5_min.devices,
                this.data.transit_period.in_15_min.devices,
                this.data.transit_period.in_60_min.devices
            ];
            this.securityPeriodchartDeviceData = [
                this.data.security_period.in_5_min.devices,
                this.data.security_period.in_15_min.devices,
                this.data.security_period.in_60_min.devices
            ];
            this.isDataAvailable = true;
          });
      });
  }

  ngOnDestroy(){
    this.alive = false; // switches your TimerObservable off
  }


 chartOptions = {
    responsive: true,
   scales: {
      yAxes: [{
         ticks: {
            beginAtZero: true
         }
      }]
   },
  };

  transitPeriodchartDeviceData = [

  ];

  securityPeriodchartDeviceData = [
  ];
  batchartLabels = ['Mean Time', 'Median Time']
  securityPeriodTableData5Min = [{data:[]}];
  securityPeriodTableData15Min = [{data:[]}];
  securityPeriodTableData60Min = [{data:[]}];

  transitPeriodTableData5Min = [{data:[]}];
  transitPeriodTableData15Min = [{data:[]}];
  transitPeriodTableData60Min = [{data:[]}];

  securityPeriodchartData5Min = [{data:[]}];
  securityPeriodchartData15Min = [{data:[]}];
  securityPeriodchartData60Min = [{data:[]}];

  transitPeriodchartData5Min = [{data:[]}];
  transitPeriodchartData15Min = [{data:[]}];
  transitPeriodchartData60Min = [{data:[]}];

  transitPeriodchartData = [

  ];

  securityPeriodchartData = [
  ];

  chartLabels = ['Last 5 Minutes', 'Last 15 Minutes', 'Last 60 Minutes'];

  onChartClick(event) {
    console.log(event);
  }
}
