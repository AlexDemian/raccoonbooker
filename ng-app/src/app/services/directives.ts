import {Directive, ElementRef, HostListener, OnChanges} from '@angular/core';
import {NgControl} from '@angular/forms';
@Directive({
  selector: '[smartFloatField]'
})
export class smartFloatFieldDirective {
  constructor(private el: ElementRef) { }

  @HostListener('input') onMyInput() {
    // ToDo: does't update NgModel
    //let value = this.el.nativeElement.value
    //value = value.replace("k", "000"); 
    //this.el.nativeElement.value = parseFloat(value).toFixed(2) || 0.00 ;
    console.log('Converted', this.el.nativeElement.value)
  }

}