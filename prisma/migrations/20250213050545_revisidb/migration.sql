/*
  Warnings:

  - You are about to drop the column `pwmLed1` on the `led` table. All the data in the column will be lost.
  - You are about to drop the column `pwmLed2` on the `led` table. All the data in the column will be lost.
  - You are about to drop the column `pwmLed3` on the `led` table. All the data in the column will be lost.
  - You are about to drop the column `pwmLed4` on the `led` table. All the data in the column will be lost.
  - You are about to drop the column `pwmLed5` on the `led` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "led" DROP COLUMN "pwmLed1",
DROP COLUMN "pwmLed2",
DROP COLUMN "pwmLed3",
DROP COLUMN "pwmLed4",
DROP COLUMN "pwmLed5";
