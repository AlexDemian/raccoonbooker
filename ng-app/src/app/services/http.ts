import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from "angular2-cookie/core";
import { Urls } from '../externalJs/django_js_reverse/js/reverse.js';

export class Entry{
    id: number;
    name: string;
    rows: Array <EntryRow>;
}

export class EntryRow{
    id: number;
    name: string;
    description: string;
    pinned: boolean;
    amount:  number;
    deleted: boolean;
    category: EntryCategory;
    entry: number;
}

export class EntryCategory {
    id: number;
    sheet: number;
    name: string;
    positive: boolean;
}

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
        return this.http.get(Urls['api-entries-list'](), {headers: this.httpHeaders})
    }

    addEntry(entry): Observable<any> {
        return this.http.post(Urls['api-entries-list'](), entry, {headers: this.httpHeaders});
    }

    updateEntry(entry): Observable<any> {
        return this.http.patch(Urls['api-entries-detail'](entry.id), entry, {headers: this.httpHeaders});
    }

    addRow(row): Observable<any> {
        console.log('Pushed row', row)
        return this.http.post(Urls['api-rows-list'](), row, {headers: this.httpHeaders});
    }

    updateRow(row): Observable<any> {
        return this.http.patch(Urls['api-rows-detail'](row.id), row, {headers: this.httpHeaders});
    }

    private handleError(error: any) {
        console.log(error);
        return Observable.throw(error.message || error);
    }
}