import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'filterObjectsByProperty', pure: false})
export class filterObjectsByPropertyPipe implements PipeTransform {
  transform(objects: any, param: string, value: any): any {
    let filtered = objects.filter(obj => obj[param] === value);
    return filtered
  }
}