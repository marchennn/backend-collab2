/*
  Warnings:

  - Added the required column `led5` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `pwmLed5` to the `led` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "led" ADD COLUMN     "led5" TEXT NOT NULL,
ADD COLUMN     "pwmLed5" TEXT NOT NULL;
