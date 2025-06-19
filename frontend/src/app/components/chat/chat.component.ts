import { CommonModule } from '@angular/common';
import { AfterViewChecked, Component, ElementRef, OnDestroy, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

interface Message {
  id: number;
  text: string;
  isUser: boolean;
  timestamp: Date;
  status?: 'sending' | 'sent' | 'delivered' | 'read';
}

@Component({
  selector: 'app-chat',
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent implements AfterViewChecked, OnDestroy {

  @ViewChild('messagesContainer') private messagesContainer!: ElementRef;
  @ViewChild('messageInput') private messageInput!: ElementRef;

  messages: Message[] = [];
  newMessage: string = '';
  messageId: number = 1;
  isTyping: boolean = false;
  isOnline: boolean = true;

  private shouldScrollToBottom = false;

  constructor() {
  }

  ngAfterViewChecked() {
    if (this.shouldScrollToBottom) {
      this.scrollToBottom();
      this.shouldScrollToBottom = false;
    }
  }

  ngOnDestroy() {
  }

  sendMessage() {
    if (this.newMessage.trim() && this.newMessage.length <= 500) {
      const userMessage = this.newMessage.trim();
      this.messages.push({
        id: this.messageId++,
        text: userMessage,
        isUser: true,
        timestamp: new Date(),
        status: 'sending'
      });

      this.newMessage = '';
      this.shouldScrollToBottom = true;

      setTimeout(() => {
        const lastMessage = this.messages[this.messages.length - 1];
        if (lastMessage) {
          lastMessage.status = 'sent';
        }
      }, 500);

      this.isTyping = true;

      setTimeout(() => {
        this.isTyping = false;
        this.addBotResponse(userMessage);
      }, 1500 + Math.random() * 1000);

      setTimeout(() => {
        this.messageInput.nativeElement.focus();
      }, 100);
    }
  }

  onInputChange() {

  }

  trackByMessageId(index: number, message: Message): number {
    return message.id;
  }

  getMessageClasses(isUser: boolean): string {
    const baseClasses = 'px-4 py-3 rounded-lg max-w-xs md:max-w-sm lg:max-w-md break-words shadow-sm';
    return isUser
      ? `${baseClasses} bg-gray-400 text-white ml-auto`
      : `${baseClasses} bg-gray-500 text-white`;
  }

  getButtonClasses(): string {
    const baseClasses = 'p-2 rounded-full transition-all duration-200';
    const enabledClasses = 'bg-pink-600 hover:bg-pink-700 text-white cursor-pointer shadow-md';
    const disabledClasses = 'bg-pink-300 text-pink-100 cursor-not-allowed';

    return `${baseClasses} ${this.newMessage.trim() ? enabledClasses : disabledClasses}`;
  }

  private addBotResponse(userMessage: string) {
    const responses = [
      'Obrigado pela sua mensagem! Vou analisar sua solicitação.',
      'Entendi sua questão. Posso ajudá-lo com isso.',
      'Ótima pergunta! Deixe-me verificar as informações para você.',
      'Recebido! Estou processando sua solicitação.',
      'Perfeito! Vou encaminhar sua demanda para o setor responsável.',
      'Compreendo sua necessidade. Vou buscar a melhor solução.',
      'Excelente! Sua solicitação foi registrada com sucesso.',
      'Obrigado por entrar em contato! Estou aqui para ajudar.'
    ];

    const randomResponse = responses[Math.floor(Math.random() * responses.length)];

    this.messages.push({
      id: this.messageId++,
      text: randomResponse,
      isUser: false,
      timestamp: new Date(),
      status: 'delivered'
    });

    this.shouldScrollToBottom = true;
  }

  private scrollToBottom(): void {
    try {
      if (this.messagesContainer) {
        const element = this.messagesContainer.nativeElement;
        element.scrollTop = element.scrollHeight;
      }
    } catch (err) {
      console.error('Erro ao fazer scroll:', err);
    }
  }

  clearChat() {
    this.messages = [];
    this.messageId = 1;
  }

  exportChat() {
    if (this.messages.length === 0) {
      return;
    }

    const chatText = this.messages.map(msg =>
      `[${msg.timestamp.toLocaleTimeString()}] ${msg.isUser ? 'Usuário' : 'Sistema'}: ${msg.text}`
    ).join('\n');

    const blob = new Blob([chatText], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `chat-${new Date().toISOString().split('T')[0]}.txt`;
    a.click();
    window.URL.revokeObjectURL(url);
  }
}
