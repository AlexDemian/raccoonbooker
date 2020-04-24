import {Directive, ElementRef, HostListener} from '@angular/core';

@Directive({
  selector: '[floatField]'
})
export class floatFieldDirective {
  constructor(private el: ElementRef) { }

  @HostListener('input') onMyInput() {
    this.el.nativeElement.value = Number(this.el.nativeElement.value) || 0 ;
  }
}