import { Component } from '@angular/core';

@Component({
  selector: 'app-my-component',
  templateUrl: './my-component.component.html',
  styleUrls: ['./my-component.component.css'],
})
export class MyComponentComponent {
  currentDate: Date;
  message: string;

  constructor() {
    this.currentDate = new Date();
    this.message = '';
  }

  onButtonClick() {
    this.message = 'Hello World!';
  }
}
