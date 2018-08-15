import {Injectable, EventEmitter} from '@angular/core'
import {Subject} from "rxjs/Subject";
import {Http, Response, Headers} from "@angular/http";
import {Observable} from "rxjs";
import {urls} from "../api-conf/api-conf";
import "rxjs/Rx";


@Injectable()
export class HomeService{
  baseUrl = urls.baseUrl;
  apiUrl = urls.apiUrl;

  constructor(private http: Http) { }

  get(): Observable<any>{
    let headers = new Headers({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });

    return this.http
      .get(this.baseUrl + 'presence_summary', {headers: headers})
      .map((res: Response) => res.json());
  }
}
