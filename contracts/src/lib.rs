use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint::entrypoint,
    entrypoint::ProgramResult,
    program::invoke,
    pubkey::Pubkey,
    rent::Rent,
    system_instruction,
    sysvar::Sysvar,
    msg,
};

entrypoint!(process_instruction);

pub fn process_instruction(
    _program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let payer = next_account_info(accounts_iter)?;           // donor
    let shelter = next_account_info(accounts_iter)?;         // verified shelter wallet
    let system_program = next_account_info(accounts_iter)?;  // system program

    let lamports = payer.lamports();

    if lamports == 0 {
        return Ok(());
    }

    msg!("AngelHavenOS: Forwarding {} lamports → {}", lamports, shelter.key);

    invoke(
        &system_instruction::transfer(payer.key, shelter.key, lamports),
        &[payer.clone(), shelter.clone(), system_program.clone()],
    )?;

    Ok(())
}
