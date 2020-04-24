import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from "angular2-cookie/core";


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
        return this.http.get('/api/booker/entries/', {headers: this.httpHeaders})
    }

    addEntry(entry): Observable<any> {
        return this.http.post('/api/booker/entries/', entry, {headers: this.httpHeaders});
    }

    updateEntry(entry): Observable<any> {
        return this.http.patch('/api/booker/entries/', entry, {headers: this.httpHeaders});
    }

    addRow(row): Observable<any> {
        console.log('Pushed row', row)
        return this.http.post('/api/booker/rows/', row, {headers: this.httpHeaders});
    }

    updateRow(row): Observable<any> {
        return this.http.patch('/api/booker/rows/'+row.id+'/', row, {headers: this.httpHeaders});
    }

    private handleError(error: any) {
        console.log(error);
        return Observable.throw(error.message || error);
    }
}