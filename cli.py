from threading import Thread

from attacker import Attacker

if __name__ == '__main__':
    import click

    from config import DEFAULT_THREADS_COUNT
    from logger import get_logger
    from utils import clear_console, cleaner, load_sites_for_attack_from_file

    log = get_logger()


    @click.command()
    @click.option('--threads_count', '-t', default=DEFAULT_THREADS_COUNT,
                  help='Количество запущенных потоков; Не импользуйте слишком большое чистло!', show_default=True)
    @click.option('--without_logger', '-wl', is_flag=True, help='Вкл/выкл логгирование;')
    def cli(threads_count, without_logger):
        clear_console()

        log.info(f"Loggers is {'stopped' if without_logger else 'started'}.")
        log.info(f"Running {threads_count} threads...")

        if without_logger:
            log.stop()
        attacker = Attacker()

        attacker.sites_for_attack = load_sites_for_attack_from_file()
        attacker.start_workers(threads_count)

        Thread(target=cleaner, daemon=True).start()


    cli()
