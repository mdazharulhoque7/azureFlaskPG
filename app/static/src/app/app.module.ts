import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ChartsModule } from 'ng2-charts';

import { AppComponent } from './app.component';
import {HeaderComponent} from './header/hader.component';
import {HomeComponent} from './home/home.component'
import {LoginComponent} from "./login/login.component";
import {HowItWorksComponent} from "./howitworks/howitworks.component";
import {CaseStudiesComponent} from "./casestudies/casestudies.component";
import {ContactComponent} from "./contact/contact.component";


import {AppRoutingModule} from "./app-routing.module";

import {AuthService} from "./auth/auth.service";
import {DropdownDirective} from "./directives/dropdown.directive";


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    LoginComponent,
    HowItWorksComponent,
    CaseStudiesComponent,
    ContactComponent,
    DropdownDirective
  ],
  imports: [
    BrowserModule,
    ChartsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
