import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

import {HomeComponent} from "./home/home.component";
import {LoginComponent} from "./login/login.component";
import {HowItWorksComponent} from "./howitworks/howitworks.component";
import {CaseStudiesComponent} from "./casestudies/casestudies.component";
import {ContactComponent} from "./contact/contact.component";


const appRoute:Routes = [
  {path:'', component:HomeComponent},
  {path:'login', component:LoginComponent},
  {path:'how_it_works', component:HowItWorksComponent},
  {path:'case_studies', component:CaseStudiesComponent},
  {path:'contact_us', component:ContactComponent},
];
@NgModule({
  imports:[RouterModule.forRoot(appRoute)],
  exports:[RouterModule]
})
export class AppRoutingModule{

}
