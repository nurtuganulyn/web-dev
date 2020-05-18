import { Component, OnInit, Input } from '@angular/core';
import { FormGroup , FormBuilder , FormControl  , Validators } from '@angular/forms';
import {User} from '../models/user';
import { Location} from '@angular/common';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  @Input() user: User;

  public login = '';
  public password = '';
  public confirm = '';
  public name = '';
  public email = '';
  constructor(private location: Location) { }

  ngOnInit(): void {
  }

  clear() {
    this.login = '';
    this.password = '';
    this.confirm = '';
    this.name = '';
    this.email = '';
  }
  goBack(): void {
    this.location.back();
  }
  signup() {
    if (!this.login || !this.password || !this.confirm) {
      alert('Please, write your login and password!');
      this.clear();
    } else if (this.password !== this.confirm) {
      alert('Passwords do not match. Try again, please!');
      this.clear();
    } else {
      alert('You were successfully logged in. Now log in our system.');
    }
  }
}
