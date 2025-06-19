
export interface ClientContact {
  id: number;
  client_name: string;
  client_number: string;
  have_art: boolean;
  tattoo_artist_wanted: string;
  status: 'waiting' | 'contacted' | 'finalized';
}

export interface StatusUpdate {
  status: 'waiting' | 'contacted' | 'finalized';
}

export enum ContactStatus {
  WAITING = 'waiting',
  CONTACTED = 'contacted',
  FINALIZED = 'finalized'
} 