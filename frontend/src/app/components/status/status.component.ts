import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ClientContactService } from '../../services/client-contact.service';
import { ClientContact } from '../../interfaces/client-contact.interface';


@Component({
  selector: 'app-status',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './status.component.html',
  styleUrl: './status.component.css'
})
export class StatusComponent implements OnInit {

  clientContacts: ClientContact[] = [];

  constructor(
    private clientContactService: ClientContactService
  ) {

  }

  ngOnInit(): void {
    this.loadClientContacts();
  }

  usuarios: ClientContact[] = [
    {
      id: 1,
      client_name: 'Pedro',
      client_number: '(51) 99999-9999',
      have_art: true,
      tattoo_artist_wanted: 'Jean Szimanski',
      status: 'waiting'
    },
    {
      id: 2,
      client_name: 'Julia',
      client_number: '(51) 88888-8888',
      have_art: false,
      tattoo_artist_wanted: 'Maria Quelipe',
      status: 'contacted'
    },
    {
      id: 3,
      client_name: 'Carlos',
      client_number: '(51) 77777-7777',
      have_art: true,
      tattoo_artist_wanted: 'Gustavo Campos',
      status: 'finalized'
    },
    {
      id: 4,
      client_name: 'Maria',
      client_number: '(51) 66666-6666',
      have_art: false,
      tattoo_artist_wanted: 'Jean Szimanski',
      status: 'contacted'
    }
  ];

  loadClientContacts(): void {
    this.clientContactService.getAllClientContacts().subscribe(
      (contacts) => {
        this.clientContacts = contacts;
        console.log('Contatos carregados:', contacts);
      },
      (error) => {
        console.error('Erro ao carregar contatos:', error);
      }
    );
  }

  refreshStatus(usuario: ClientContact): void {
    console.log(`Atualizando status de ${usuario.client_name}`);

    const statusCycle: Record<string, { status: 'waiting' | 'contacted' | 'finalized' }> = {
      'waiting': { status: 'contacted' },
      'contacted': { status: 'finalized' },
      'finalized': { status: 'waiting' }
    };

    const nextStatus = statusCycle[usuario.status];
    if (nextStatus) {
      // Atualizar no backend
      this.clientContactService.updateClientContactStatus(usuario.id, nextStatus.status).subscribe(
        (updatedContact) => {
          // Atualizar o objeto local
          usuario.status = updatedContact.status;
          console.log('Status atualizado com sucesso:', updatedContact);
        },
        (error) => {
          console.error('Erro ao atualizar status:', error);
        }
      );
    }
  }

  sair(): void {
  }

  getStatusColor(status: string): string {
    const colors: Record<string, string> = {
      'waiting': 'text-orange-500',
      'contacted': 'text-green-500',
      'finalized': 'text-blue-500'
    };
    return colors[status] || 'text-gray-500';
  }

  getStatusText(status: string): string {
    const texts: Record<string, string> = {
      'waiting': 'Aguardando Contato',
      'contacted': 'Contato Realizado',
      'finalized': 'Atendimento Finalizado'
    };
    return texts[status] || 'Status Desconhecido';
  }
}
