import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class BookerEntriesAPI{
    constructor(private http: HttpClient){ }
    httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
    getTables(): Observable<any> {
        return this.http.get('/api/booker/entries/', {headers: this.httpHeaders});
    }
}