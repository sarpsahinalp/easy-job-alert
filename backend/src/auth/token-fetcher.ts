import { $ } from "bun";

export async function fetchToken(command: string, args: string[] = []): Promise<string> {
  const result = await $`${command} ${args}`.text();
  return result.trim();
}
