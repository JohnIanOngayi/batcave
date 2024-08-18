import { RowID, RowElement } from "./interface";

export function insertRow(row: RowElement): number;

export function deleteRow(rowId: number): void;

export function updateRow(rowId: number, row: RowElement): number;
