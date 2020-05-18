import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from './models/user';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private usersUrl = 'api/users';  // URL to web api
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
   ) { }

   getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.usersUrl);
  }

  /** GET hero by id. Will 404 if id not found */
   getUser(id: number): Observable<User> {
  const url = `${this.usersUrl}/${id}`;
  return this.http.get<User>(url);
   }

   /** PUT: update the hero on the server */
   updateUser(user: User): Observable<any> {
  return this.http.put(this.usersUrl, user, this.httpOptions);
   }
   addUser(user: User): Observable<User> {
    return this.http.post<User>(this.usersUrl, user, this.httpOptions);
  }
}
