import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable()
export class BookerEntriesAPI{

    constructor(private http: HttpClient){ }

    getTables(){
        return this.http.get('api/booker/entries/?format=json')
    }
}