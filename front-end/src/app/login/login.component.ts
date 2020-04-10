import { Component, OnInit } from '@angular/core';
import { Location} from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public login = '';
  public password = '';
  constructor(private location: Location) { }

  ngOnInit(): void {
  }
  clear() {
    this.login = '';
    this.password = '';
  }
  goBack(): void {
    this.location.back();
  }
  logIn() {
    if (!this.login || !this.password) {
      alert('Please, write your login and password!');
      this.clear();
    } else {
      alert('You were successfully logged in. Now log in our system.');
    }
  }
}
