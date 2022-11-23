import { writable } from "svelte/store";

export const step = writable(0);
export const artist_choose = writable('');
export const lyrics = writable('');