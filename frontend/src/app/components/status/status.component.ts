import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

interface Usuario {
  nome: string;
  tabuador: string;
  status: 'aguardando' | 'realizado' | 'finalizado';
  statusTexto: string;
  statusColor: string;
}

@Component({
  selector: 'app-status',
  imports: [CommonModule],
  templateUrl: './status.component.html',
  styleUrl: './status.component.css'
})
export class StatusComponent {

  usuarios: Usuario[] = [
    {
      nome: 'Pedro',
      tabuador: 'Tabuador: xxxx',
      status: 'aguardando',
      statusTexto: 'Aguardando Contato',
      statusColor: 'text-orange-500'
    },
    {
      nome: 'Julia',
      tabuador: 'Tabuador: xxxx',
      status: 'realizado',
      statusTexto: 'Contato Realizado',
      statusColor: 'text-green-500'
    },
    {
      nome: 'Carlos',
      tabuador: 'Tabuador: xxxx',
      status: 'finalizado',
      statusTexto: 'Atendimento Finalizado',
      statusColor: 'text-blue-500'
    },
    {
      nome: 'Maria',
      tabuador: 'Tabuador: xxxx',
      status: 'realizado',
      statusTexto: 'Contato Realizado',
      statusColor: 'text-green-500'
    }
  ];

  refreshStatus(usuario: Usuario): void {
    // Simula uma atualização de status
    console.log(`Atualizando status de ${usuario.nome}`);

    // Exemplo de lógica para ciclar entre os status
    const statusCycle: Record<string, { status: 'aguardando' | 'realizado' | 'finalizado', texto: string }> = {
      'aguardando': { status: 'realizado', texto: 'Contato Realizado' },
      'realizado': { status: 'finalizado', texto: 'Atendimento Finalizado' },
      'finalizado': { status: 'aguardando', texto: 'Aguardando Contato' }
    };

    const nextStatus = statusCycle[usuario.status];
    if (nextStatus) {
      usuario.status = nextStatus.status;
      usuario.statusTexto = nextStatus.texto;
    }

    // Aqui você pode adicionar uma chamada para API
    // this.usuarioService.updateStatus(usuario.id, usuario.status);
  }

  sair(): void {
    // Lógica para sair da aplicação
    console.log('Saindo da aplicação');
    // Exemplo: this.router.navigate(['/login']);
  }

  // Método auxiliar para obter a cor do status
  getStatusColor(status: string): string {
    const colors: Record<string, string> = {
      'aguardando': 'text-orange-500',
      'realizado': 'text-green-500',
      'finalizado': 'text-blue-500'
    };
    return colors[status] || 'text-gray-500';
  }
}
