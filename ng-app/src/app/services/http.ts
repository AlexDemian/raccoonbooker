import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from "angular2-cookie/core";

@Injectable()
export class BookerEntriesAPI{
    constructor(private http: HttpClient, private _cookieService: CookieService){ }
    httpHeaders = new HttpHeaders({
        'Content-Type': 'application/json',
        "X-CSRFToken": this.getCookie('csrftoken')
    });

    getCookie(key: string) {
        return this._cookieService.get(key);
    }

    getEntries(): Observable<any> {
        return this.http.get('/api/booker/entries/', {headers: this.httpHeaders});
    }

    addEntrie(entrie_name, sheet_id): Observable<any> {
        return this.http.post('/api/booker/entries/', {
            headers: this.httpHeaders,
            data: {
                period: '01-01-2020',
                name: 'Foo',
                sheet: 1
            }
        });
    }

    addRow(row): Observable<any> {
        return this.http.post('/api/booker/rows/', row, {headers: this.httpHeaders});
    }
}