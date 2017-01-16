from bitcoin import sign
from tx import TX
from wallet.wallet import generate_std_scriptpubkey, get_priv_key_hex


def build_raw_tx(prev_tx_id, prev_out_index, value, src_btc_addr, dest_btc_addr):

    assert len(prev_tx_id) == len(prev_out_index) == len(value)

    scriptPubKey = []
    for i in range(len(dest_btc_addr)):
        scriptPubKey.append(generate_std_scriptpubkey(dest_btc_addr[i]))

    tx = TX()
    tx.build_default_tx(prev_tx_id, prev_out_index, value, scriptPubKey)

    signed_tx = ""
    for i in range(len(src_btc_addr)):
        pirv_key = src_btc_addr[i] + "/sk.pem"
        priv_key_hex = get_priv_key_hex(pirv_key)
        signed_tx = sign(tx.hex, 0, priv_key_hex)

    tx.print_elements()
    return signed_tx

