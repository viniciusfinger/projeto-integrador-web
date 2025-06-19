import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { 
  ClientContact, 
  StatusUpdate 
} from '../interfaces/client-contact.interface';

@Injectable({
  providedIn: 'root'
})
export class ClientContactService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }


  getAllClientContacts(): Observable<ClientContact[]> {
    return this.http.get<ClientContact[]>(`${this.apiUrl}/client-contacts`);
  }


  updateClientContactStatus(id: number): Observable<ClientContact> {
    return this.http.put<ClientContact>(`${this.apiUrl}/client-contacts/${id}/status`, {});
  }
} 